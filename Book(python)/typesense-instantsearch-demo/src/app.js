import { Buffer } from "buffer";
window.Buffer = Buffer;
const { algoliasearch, instantsearch } = window;

import TypesenseInstantSearchAdapter from "typesense-instantsearch-adapter";

const typesenseInstantsearchAdapter = new TypesenseInstantSearchAdapter({
  server: {
    apiKey: "308", // Be sure to use the search-only-api-key
    nodes: [
      {
        host: "localhost",
        port: 8108,
        protocol: "http"
      }
    ]
  },
  // The following parameters are directly passed to Typesense's search API endpoint.
  //  So you can pass any parameters supported by the search endpoint below.
  //  query_by is required.
  additionalSearchParameters: {
    query_by: "title,authors"
  }
});
const searchClient = typesenseInstantsearchAdapter.searchClient;

const search = instantsearch({
  searchClient,
  indexName: "books"
});


search.addWidgets([
  instantsearch.widgets.searchBox({
    container: '#searchbox',
  }),
  instantsearch.widgets.hits({
    container: '#hits',
    templates: {
      item: `
        <div>
          <img src="{{image_url}}" align="left" alt="{{title}}" />
          <div class="hit-content">
            <div class="hit-name">
              {{#helpers.highlight}}{ "attribute": "title" }{{/helpers.highlight}}
            </div>
            <div class="hit-authors">
              Author: {{#helpers.highlight}}{ "attribute": "authors" }{{/helpers.highlight}}
            </div>
            <div class="hit-year">Published: {{publication_year}}</div>
            <div class="hit-rating">Rating: {{average_rating}} ⭐</div>
            <div class="hit-reviews">Reviews: {{ratings_count}}</div>
          </div>
        </div>

      `,
    },
  }),
  instantsearch.widgets.pagination({
    container: '#pagination',
  }),
]);

search.start();

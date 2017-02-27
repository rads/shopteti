const React = require('react');
const ReactDOM = require('react-dom');
const IndexPage = require('./index_page');

const container = document.getElementById('Container');
const element = <IndexPage />;

ReactDOM.render(element, container);
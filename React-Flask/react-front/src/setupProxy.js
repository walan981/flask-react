
//Configura a URL do banco de dados de onde o React vai se comunicar

const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = function(app) {
  app.use(
    '/api',
    createProxyMiddleware({
      target: 'http://127.0.0.1:5000/',
      changeOrigin: true,
    })
  );
};
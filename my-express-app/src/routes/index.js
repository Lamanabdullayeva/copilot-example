function setupRoutes(app) {
    const controller = require('../controllers/index');

    app.get('/', controller.home);
    app.get('/about', controller.about);
    app.get('/contact', controller.contact);
}

module.exports = setupRoutes;
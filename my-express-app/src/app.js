const express = require('express');
const routes = require('./routes/index');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Routes
app.use('/api', routes());

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
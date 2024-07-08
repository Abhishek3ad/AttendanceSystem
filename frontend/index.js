const functions = require('firebase-functions');
const { Nuxt } = require('nuxt');
const express = require('express');
const { https } = functions;

const app = express();

const nuxtConfig = {
    dev: false,
    buildDir: '.nuxt',
    build: {
        publicPath: '/assets/',
    },
};

const nuxt = new Nuxt(nuxtConfig);

app.use(nuxt.render);

exports.ssr = https.onRequest(app);

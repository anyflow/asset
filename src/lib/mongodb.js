'use strict';

const mongoose = require('mongoose');

mongoose.Promise = global.Promise;

let loaded = false;

async function init() {
  if (!loaded) {
    await mongoose.connect('mongodb://localhost/realty', {
      useNewUrlParser: true,
      useUnifiedTopology: true
    });

    const ApartmentSchema = new mongoose.Schema({
      apartment: String,
      dealedAt: String,
      price: Number,
      floor: Number,
      landAddress: String,
      exclusiveArea: Number,
      builtAt: Number,
      localCode: Number,
      address_1: String,
      address_2: String,
      address_3: String,
    });

    mongoose.model('Apartment', ApartmentSchema);

    loaded = true;
  }

  return {
    Apartment: mongoose.model('Apartment'),
  };
}

async function removeAll() {
  const {
    Apartment
  } = await mongodb.init();

  return await Apartment.remove({});
}

module.exports = {
  init,
  removeAll,
  disconnect: mongoose.disconnect
};
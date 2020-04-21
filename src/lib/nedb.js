'use strict';

const Datastore = require('nedb-promises');

// 행정코드 URL : https://www.mois.go.kr/frt/bbs/type001/commonSelectBoardArticle.do?bbsId=BBSMSTR_000000000052&nttId=61552

let admincode = null;
let apartment = null;

let loaded = false;
if (!loaded) {
  admincode = Datastore.create({
    filename: `${__dirname}/../../db/admincode.nedb`,
    autoload: true
  });

  apartment = Datastore.create({
    filename: `${__dirname}/../../db/apartment.nedb`,
    autoload: true
  });


  loaded = true;
}

module.exports = {
  admincode,
  apartment
};
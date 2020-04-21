'use strict';

const rp = require('request-promise');
const querystring = require('querystring');

const {
  runAsync
} = require('./lib/utility');
const {
  admincode,
  apartment
} = require('./lib/nedb');

const mongodb = require('./lib/mongodb');

const serviceKey = 'dL%2BzS3fmxWfJeusp7G7KpvuVKvUk6vySAmXeZvDfsnhpXPLn8OniwNon01BNcpfGt1c1Eoh0fgNFOgTMVmd6Mw%3D%3D';

let totalCount = 0;


async function transaction(LAWD_CD, DEAL_YMD) {
  // https://www.data.go.kr/subMain.jsp#/L3B1YnIvcG90L215cC9Jcm9zTXlQYWdlL29wZW5EZXZEZXRhaWxQYWdlJEBeMDgyTTAwMDAxMzBeTTAwMDAxMzUkQF5wdWJsaWNEYXRhRGV0YWlsUGs9dWRkaTpiYmIzMzY4Mi1kN2UxLTQ2YTQtOGY3My1iZDVlN2RhMjI0ZDNfMjAxNjAyMDEwOTI4JEBecHJjdXNlUmVxc3RTZXFObz0zMzA2OTYwJEBecmVxc3RTdGVwQ29kZT1TVENEMDE=

  const code = await admincode.findOne({
    '행정동코드': new RegExp('^' + LAWD_CD)
  });

  const uri = `http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade`;
  const res = await rp({
    uri,
    qs: {
      LAWD_CD,
      DEAL_YMD,
      ServiceKey: querystring.unescape(serviceKey),
    },
    json: true
  });

  if (res.response.header.resultCode !== '00') {
    throw new Error('Failed to retrieve!');
  }

  if (res.response.body.totalCount <= 0) {
    console.log(`[${LAWD_CD}|${DEAL_YMD}] No records`);
    return;
  }

  const {
    Apartment
  } = await mongodb.init();

  const arr = res.response.body.totalCount === 1 ? [res.response.body.items.item] : res.response.body.items.item;

  await Apartment.create(arr.map(val => {
    return {
      'apartment': _str(val['아파트']),
      'dealedAt': new Date(val['년'], val['월'], val['일']).toLocaleDateString(),
      'price': _num(val['거래금액'].trim().replace(',', '')),
      'floor': _num(val['층']),
      'landAddress': _str(val['지번']),
      'exclusiveArea': _num(val['전용면적']),
      'builtAt': _num(val['건축년도']),
      'localCode': _num(val['지역코드']),
      'address_1': _str(code['시도명']),
      'address_2': _str(code['시군구명']),
      'address_3': _str(code['읍면동명']),
      'address_4': _str(code['동리명']),
    };
  }));

  console.log(`[${LAWD_CD}|${DEAL_YMD}|${code['시도명']}|${code['시군구명']}|${code['읍면동명']}] ${res.response.body.totalCount} | ${totalCount += res.response.body.totalCount}`);
}

function _str(val) {
  return val ? val.toString() : val;
}

function _num(val) {
  return val ? Number(val) : val;
}

function yearMonths() {

  function _c(val) {
    return val < 10 ? '0' + val : val.toString();
  }

  const ret = [];

  for (let y = 0; y <= 20; ++y) {
    for (let m = 1; m <= 12; ++m) {
      ret.push('20' + _c(y) + _c(m));
    }
  }

  return ret;
}

async function localCodes(gte) {
  const set = new Set();

  const codes = await admincode.find({
    '말소일자': {
      $exists: false
    }
  });

  for (const code of codes) {
    set.add(code['행정동코드'].substring(0, 5));
  }

  const ret = Array.from(set).sort();

  return gte ? ret.filter(item => item >= gte) : ret;
}

async function getAll(args) {
  const codes = await localCodes(args[0]);
  console.log(`code size : ${codes.length}`);

  const yms = yearMonths();
  console.log(`yearMonth size : ${yms.length}`);

  console.log(`transaction count : ${yms.length * codes.length}`);

  let index = 0;
  for (const code of codes) {
    console.log(`code index : ${++index} / ${codes.length}`);

    for (const ym of yms) {
      if (code <= args[0] && ym <= args[1]) continue;

      await transaction(code, ym);
    }
  }
}

runAsync(getAll, '47110', '200002');

// runAsync(async () => {
//   const {
//     Apartment
//   } = await mongodb.init();

//   const curr = await apartment.find({}).sort({
//     localCode: 1
//   }).exec();

//   let index = 0;
//   let items = [];

//   for (const item of curr) {
//     delete item['_id'];
//     item['floor'] = Number(item['floor']);

//     items.push(item);

//     console.log(`${++index} / ${curr.length}`);

//     if (index % 20000 === 0 || index === curr.length) {
//       await Apartment.create(items);
//       console.log(`SAVED --------------------------------------------------------------`);
//       items = [];
//     }
//   }

//   // await Apartment.deleteMany({});

//   console.log(`doc count : ${await Apartment.countDocuments({})}`);
//   await mongodb.disconnect();
// });


// runAsync(async () => {
//   const {
//     Apartment
//   } = await mongodb.init();

//   const res = await Apartment.find({
//     localCode: 11740
//   });

//   console.log(res);

//   await mongodb.disconnect();
// });
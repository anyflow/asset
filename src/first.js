'use strict';

const rp = require('request-promise');
const qs = require('querystring');
const codeJson = require('../code.json');

const {
  admincode
} = require('./lib/nedb');

function runAsync(predicate) {
  (async () => await predicate())();
}

const serviceKey = 'SrktWNndsgtkuO%2Ft4y7bcaG5e%2BE2UtSwqadjbfaLoHnyLW1JkeSPFtQf7fHPtB%2FUTqplmcrnr7LqTdMLW6Mjaw%3D%3D';

async function first() {
  let query = qs.stringify({
    DEAL_YMD: '201512',
    LAWD_CD: '41465',
    ServiceKey: qs.unescape(serviceKey),
  });

  const uri = `http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade?${query}`;
  const res = await rp({
    uri,
    json: true
  });

  console.log(JSON.stringify(res, null, 2));
}

async function temp() {
  await admincode.insert(codeJson);
}

runAsync(temp);
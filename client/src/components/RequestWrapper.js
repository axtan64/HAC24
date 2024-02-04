import axios from "axios";

export default class RequestWrapper {
    constructor(url, options = {}) {
      if(!url) throw new Error("Request: url not provided");
      options.url = url;
      options.method ||= 'get';
      return axios(options)
    }
  }
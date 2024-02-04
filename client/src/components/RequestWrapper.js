module.exports = class RequestWrapper {
  constructor(url, options = {}) {
    if (!url) throw new Error("Request: url not provided");

    this.url = url;
    this.options = {
      method: options.method || 'GET',
      headers: options.headers || {},
      body: options.data || null,
    };

    return this.sendRequest();
  }

  async sendRequest() {
    try {
      const response = await fetch(this.url, this.options);

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const data = await response.json();

      return data;
    } catch (error) {
      throw new Error(`Request failed: ${error.message}`);
    }
  }
};
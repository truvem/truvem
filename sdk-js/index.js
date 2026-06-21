const axios = require('axios');

class Truvem {
    constructor(apiKey = null, baseUrl = 'https://truvem.onrender.com') {
        this.apiKey = apiKey;
        this.baseUrl = baseUrl;
        this.headers = apiKey ? { 'x-api-key': apiKey } : {};
    }

    async register(email) {
        const resp = await axios.post(`${this.baseUrl}/v1/register`, { email });
        if (resp.data.api_key) {
            this.apiKey = resp.data.api_key;
            this.headers = { 'x-api-key': this.apiKey };
        }
        return resp.data;
    }

    async remember(agentId, content) {
        const resp = await axios.post(
            `${this.baseUrl}/v1/memory/write`,
            { agent_id: agentId, content },
            { headers: this.headers }
        );
        return resp.data;
    }

    async recall(agentId) {
        const resp = await axios.post(
            `${this.baseUrl}/v1/memory/read`,
            { agent_id: agentId },
            { headers: this.headers }
        );
        return resp.data;
    }

    async forget(memoryId) {
        const resp = await axios.delete(
            `${this.baseUrl}/v1/memory/forget`,
            { data: { memory_id: memoryId }, headers: this.headers }
        );
        return resp.data;
    }

    async search(agentId, query) {
        const resp = await axios.post(
            `${this.baseUrl}/v1/memory/search`,
            { agent_id: agentId, query },
            { headers: this.headers }
        );
        return resp.data;
    }
}

module.exports = Truvem;

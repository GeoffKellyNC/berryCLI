#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <curl/curl.h>
#include "json.hpp"

using json = nlohmann::json;

class Lifex {
public:
    Lifex(const std::string& apiKey)
        : _apiKey(apiKey), _baseURL("https://api.lifx.com/v1/lights"), _headers()
    {
        _headers.push_back("accept: text/plain");
        _headers.push_back("content-type: application/json");
        std::string authHeader = "Authorization: Bearer " + _apiKey;
        _headers.push_back(authHeader);
    }

    std::vector<std::unordered_map<std::string, std::string>> getDevices() {
        CURL* curl = curl_easy_init();
        if (!curl) {
            std::cerr << "Failed to initialize cURL" << std::endl;
            return {};
        }

        std::string url = _baseURL + "/all";
        std::string response;
        long httpCode = 0;

        curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
        curl_easy_setopt(curl, CURLOPT_HTTPHEADER, _headers);
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, writeCallback);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &response);
        curl_easy_setopt(curl, CURLOPT_USERAGENT, "libcurl-agent/1.0");

        CURLcode res = curl_easy_perform(curl);
        curl_easy_getinfo(curl, CURLINFO_RESPONSE_CODE, &httpCode);
        curl_easy_cleanup(curl);

        if (res != CURLE_OK) {
            std::cerr << "cURL error: " << curl_easy_strerror(res) << std::endl;
            return {};
        }

        if (httpCode != 200) {
            std::cerr << "HTTP error: " << httpCode << std::endl;
            return {};
        }

        json j = json::parse(response);
        return j.get<std::vector<std::unordered_map<std::string, std::string>>>();
    }

    void turnOff(const std::string& lightId) {
        CURL* curl = curl_easy_init();
        if (!curl) {
            std::cerr << "Failed to initialize cURL" << std::endl;
            return;
        }

        std::string url = _baseURL + "/id:" + lightId + "/state";
        std::string payload = "{\"duration\":1,\"fast\":true,\"power\":\"off\"}";
        long httpCode = 0;

        curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
        curl_easy_setopt(curl, CURLOPT_CUSTOMREQUEST, "PUT");
        curl_easy_setopt(curl, CURLOPT_HTTPHEADER, _headers);
        curl_easy_setopt(curl, CURLOPT_POSTFIELDS, payload.c_str());
        curl_easy_setopt(curl, CURLOPT_USERAGENT, "libcurl-agent/1.0");

        CURLcode res = curl_easy_perform(curl);
        curl_easy_getinfo(curl, CURLINFO_RESPONSE_CODE, &httpCode);
        curl_easy_cleanup(curl);

        if (res != CURLE_OK) {
            std::cerr << "cURL error: " << curl_easy_strerror(res) << std::endl;
            return;
        }

        if (httpCode != 200) {
            std::cerr << "HTTP error: " << httpCode << std::endl;
            return;
        }

        std::cout << "Turned off light " << lightId << std::endl;
    }

    void turnOn(const std::string& lightId) {
        CURL* curl = curl_easy_init();
        if (!curl) {
            std::cerr << "Failed to initialize cURL" << std::endl;
            return;
        }

        std::string url = _baseURL + "/id:" + lightId + "/state";
        std::string payload = "{\"duration\":1,\"fast\":true,\"power\":\"on\"}";
        long httpCode = 0;

        curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
        curl_easy_setopt(curl, CURLOPT_CUSTOMREQUEST, "PUT");
        curl_easy_setopt(curl, CURLOPT_HTTPHEADER, _headers);
        curl_easy_setopt(curl, CURLOPT_POSTFIELDS, payload.c_str());
        curl_easy_setopt(curl, CURLOPT_USERAGENT, "libcurl-agent/1.0");
        
        CURLcode res = curl_easy_perform(curl);
        curl_easy_getinfo(curl, CURLINFO_RESPONSE_CODE, &httpCode);
        curl_easy_cleanup(curl);

        if (res != CURLE_OK) {
            std::cerr << "cURL error: " << curl_easy_strerror(res) << std::endl;
            return;
        }

        if (httpCode != 200) {
            std::cerr << "HTTP error: " << httpCode << std::endl;
            return;
        }

        std::cout << "Turned on light " << lightId << std::endl;
    }



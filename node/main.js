const axios = require('axios');



const light = async (power, key, id) => {

    const options = {
      method: 'PUT',
      url: `https://api.lifx.com/v1/lights/id%${id}/state`,
      headers: {
        accept: 'text/plain',
        'content-type': 'application/json',
        Authorization: `Bearer ${key}`
      },
      data: {duration: 1, fast: true, power: power}
    };
    
    axios
      .request(options)
      .then(function (response) {
        console.log(response.data);
      })
      .catch(function (error) {
        console.error(error);
      });

}

light('on')







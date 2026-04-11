const zlib = require('zlib');

const compressData = (data) => {
    return new Promise((resolve, reject) => {
        zlib.gzip(data, (err, buffer) => {
            if (err) return reject(err);
            resolve(buffer);
        });
    });
};

const decompressData = (buffer) => {
    return new Promise((resolve, reject) => {
        zlib.gunzip(buffer, (err, decompressed) => {
            if (err) return reject(err);
            resolve(decompressed.toString());
        });
    });
};

const normalizeStoreName = (storeName) => {
    if (!storeName) {
        return "sessions";
    }
    const normalizedStoreName = storeName.split(' ')[0].toLowerCase();
    if (["sessions", "templates", "names", "themes"].includes(normalizedStoreName)) {
        return normalizedStoreName;
    }
    return null;
};

module.exports = {
    compressData,
    decompressData,
    normalizeStoreName
};

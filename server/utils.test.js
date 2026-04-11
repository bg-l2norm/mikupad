const { test, describe } = require('node:test');
const assert = require('node:assert');
const { compressData, decompressData, normalizeStoreName } = require('./utils');

describe('Utility Functions', () => {
    describe('compressData and decompressData', () => {
        test('should compress and decompress data correctly', async () => {
            const originalData = 'Hello, world! This is a test string for compression.';
            const compressed = await compressData(originalData);
            assert.ok(Buffer.isBuffer(compressed));
            assert.ok(compressed.length > 0);

            const decompressed = await decompressData(compressed);
            assert.strictEqual(decompressed, originalData);
        });

        test('should handle empty strings', async () => {
            const originalData = '';
            const compressed = await compressData(originalData);
            const decompressed = await decompressData(compressed);
            assert.strictEqual(decompressed, originalData);
        });

        test('should handle large data', async () => {
            const originalData = 'A'.repeat(100000);
            const compressed = await compressData(originalData);
            const decompressed = await decompressData(compressed);
            assert.strictEqual(decompressed, originalData);
        });

        test('decompressData should reject invalid buffer', async () => {
            const invalidBuffer = Buffer.from('not a gzip buffer');
            await assert.rejects(decompressData(invalidBuffer));
        });
    });

    describe('normalizeStoreName', () => {
        test('should return "sessions" for undefined or null storeName', () => {
            assert.strictEqual(normalizeStoreName(undefined), 'sessions');
            assert.strictEqual(normalizeStoreName(null), 'sessions');
            assert.strictEqual(normalizeStoreName(''), 'sessions');
        });

        test('should normalize valid store names', () => {
            assert.strictEqual(normalizeStoreName('sessions'), 'sessions');
            assert.strictEqual(normalizeStoreName('Sessions'), 'sessions');
            assert.strictEqual(normalizeStoreName('TEMPLATES'), 'templates');
            assert.strictEqual(normalizeStoreName('names'), 'names');
            assert.strictEqual(normalizeStoreName('themes'), 'themes');
        });

        test('should handle store names with spaces or extra characters', () => {
            assert.strictEqual(normalizeStoreName('sessions extra'), 'sessions');
            assert.strictEqual(normalizeStoreName('templates 123'), 'templates');
        });

        test('should return null for invalid store names', () => {
            assert.strictEqual(normalizeStoreName('invalid'), null);
            assert.strictEqual(normalizeStoreName('randomStore'), null);
        });
    });
});

class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        // Create map to store instances of s and t
        // Iterate through s and store items in sMap
        // Iterate through t and store items in tMap

        // Compare two maps
        // We'd look at keys method to make sure values and keys are same

        const sMap = {};
        const tMap = {};

        for (const sItem of s) {
            sMap[sItem] = sMap[sItem] || 0 + 1;
        }

        for (const tItem of t) {
            tMap[tItem] = tMap[tItem] || 0 + 1;
        }

        // First make sure length matches
        if (sMap.length !== tMap.length) {
            return false;
        }

        // Then iterate over keys for each array
        for (const [key, value] of Object.entries(sMap)) {
            if (!key in tMap || tMap[key] != value) {
                return false;
            }
        }

        // Otherwise, we can return true
        return true;
    }
}

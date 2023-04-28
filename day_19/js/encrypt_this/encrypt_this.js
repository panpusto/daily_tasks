// Description:
// ENCRYPT THIS!
// You want to create secret messages which can be deciphered by the decipherThis function! 
// Here are the conditions:

// Your message is a string containing space separated words.
// You need to encrypt each word in the message using the following rules:

// The first letter must be converted to its ASCII code.
// The second letter must be switched with the last letter
// Keepin' it simple: There are no special characters in the input.

// Examples:
// encryptThis("Hello") === "72olle"
// encryptThis("good") === "103doo"
// encryptThis("hello world") === "104olle 119drlo"

// solution
const encryptThis = (text) => {
    return text
        .split(' ')
        .map(elem => {
            if (elem.length === 1) return elem.charCodeAt(0);
            if (elem.length === 2) return `${elem[0].charCodeAt(0)}${elem[1]}`;
            if (elem.length === 3) return `${elem[0].charCodeAt(0)}${elem.slice(-1)}${elem[1]}`;
            if (elem.length > 3) return `${elem[0].charCodeAt(0)}${elem.slice(-1)}${elem.slice(2, -1)}${elem[1]}`
        })
        .join(' ');
};

// 
// DECRYPT THIS!
// You are given a secret message you need to decipher. Here are the things you need to know to decipher it:

// For each word:
// the second and the last letter is switched (e.g. Hello becomes Holle)
// the first letter is replaced by its character code (e.g. H becomes 72)
// Note: there are no special characters used, only letters and spaces

// Examples
// decipherThis('72olle 103doo 100ya'); // 'Hello good day'
// decipherThis('82yade 115te 103o'); // 'Ready set go'

const decipherThis = (str) => {
    return str
        .split(' ')
        .map(elem => elem
            .replace(/^\d+/, num => String.fromCharCode(num))
            .replace(/^(.)(.)(.*)(.)$/, '$1$4$3$2')
        )
        .join(' ')
};


module.exports = {
    encryptThis,
    decipherThis
}
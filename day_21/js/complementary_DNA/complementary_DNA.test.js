const DNAStrand = require('./complementary_DNA');

test('Returns complementary DNA', () => {
    expect(DNAStrand("AAAA")).toEqual("TTTT");
    expect(DNAStrand("ATTGC")).toEqual("TAACG");
    expect(DNAStrand("GTAT")).toEqual("CATA"); 
});
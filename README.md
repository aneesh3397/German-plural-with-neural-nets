# German-plural-with-neural-nets
The list of German plural inflections contains a minority default; an inflection with low frequency but high productivity. This project is designed to see if a neural net can learn a minority default. 

Neural nets are remarkably successful at learning the morphology of languages. The reason for this is that the various inflections that denote tense, gender, number etc are often informed by phonological features. For example English has three plural inflections- /s/ as in cat-cats, /z/ as in dog-dogs and /ɪz/ as in kiss-kisses. We can see that in a word like 'kiss' the fact that the word end with an 's' can be used as a feature to trigger the /ɪz/ inflection. 

The German plural is a bit more complicated. There are a total of 7 inflections, listed below with their frequencies:

-s: 7.4%

-n: 28.7%

-e: 17%

-e + umlaut: 17%

null: 15%

umlaut: 2.5%

-er+umlaut: 12.3%

(frequencies obtained from Bittner and Köpcke, 2001)

As mentioned above, -s acts a minority default, meaning that while it's frequency is low, when presented with a new word, a German speaker's first tendency in forming the plural would be to inflect with -s. 

The training data consists of feature vectors with 20 features that can take on a value of 1 or 0. 7 prototypes were randomly generated to simulate the 7 inflectional classes. These can be found in prototypes.txt. There are two training sets, input.txt and input2.txt. Each training example was obtained by taking it's respective prototype and flipping each feature with a probability of 0.1. The training examples therefore resemble, but aren't identical to the prototypes, very much capturing the structure of natural language in which words that receive the same inflection tend to have similar phonological structure. The only difference between input.txt and input2.txt is that in input2.txt, the training examples for the -s class were generated randomly as opposed to being based off the prototype. 

The test data consists of 170 test items. Out of these, the first 70 are based off the 7 prototypes. The remaining 100 are randomly generated, intended to acts as novel forms that a native speaker hasn't seen before. 

Results:

When trained on input.txt, the following results were obtained:

Results on test examples generated from prototypes (first 70): 

-s :  10
-n :  10
-e :  9
-e+umlaut :  12
null :  9
umlaut :  7
-er+umlaut :  11
No marking :  2
Double marking :  0


Results on randomly generated test examples (remaining 100): 

-s :  10
-n :  8
-e :  4
-e+umlaut :  15
null :  6
umlaut :  0
-er+umlaut :  10
No marking :  45
Double marking :  2

We see that there is no preference for -s when it comes to marking novel forms. The model therefore hasn't learnt the minority default. When trained on input2txt however, the following results are obtained:

Results on test examples generated from prototypes: 

-s :  7
-n :  10
-e :  11
-e+umlaut :  12
null :  9
umlaut :  2
-er+umlaut :  11
No marking :  8
Double marking :  0


Results on randomly generated test examples: 

-s :  30
-n :  2
-e :  1
-e+umlaut :  9
null :  6
umlaut :  0
-er+umlaut :  3
No marking :  46
Double marking :  3

We see that when trained on input2, there is a preference for marking novel forms with -s (30 inflections). This is attributed to the fact that in input2, the -s training examples are randomly generated. Since the net is being trained on a more general
class now, ‘-s’ is preferred as the default inflection because the randomly generated novel tokens would be more similar to the ‘-s’ class than any other. With the correct training data, the model is able to learn the minority default. 

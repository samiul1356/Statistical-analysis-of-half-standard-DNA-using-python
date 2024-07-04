# Statistical-analysis-of-half-standard-DNA-using-python
there is some codes to analyse half standard DNA with statistics, 
  igygtuy

  
## Pecuiliar Half standard DNA analysis w2 m 1.3

Module 1.3.13: Pecuiliar statistics of forward & reverse
This idea motivates the following algorithm, in which we only need to consider two symbols each time we slide the window.  It uses a form of range,
for i in range(a, b)
in which we consider values of i starting with a and ending with b-1.
def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    # look at the first half of Genome to compute first array value
    array[0] = PatternCount(symbol, Genome[0:n//2])
    for i in range(1, n):
        # start by setting the current array value equal to the previous array value
        array[i] = array[i-1]

        # the current array value can differ from the previous array value by at most 1
        if ExtendedGenome[i-1] == symbol:
            array[i] = array[i]-1
        if ExtendedGenome[i+(n//2)-1] == symbol:
            array[i] = array[i]+1
    return array
Code Challenge (1 point): Re-type this algorithm into the code window below. Then add this function to Replication.py.
Click here for this problem's test datasets.
Sample Input:
AAAAGGGG
A
Sample Output:
{0: 4, 1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3}
Coursera course Link of module 1.3 https://cogniterra.org/lesson/30252/step/13?unit=22340
Exam title: Peculiar Statistics of the Forward and Reverse Half-Strands · Cogniterra



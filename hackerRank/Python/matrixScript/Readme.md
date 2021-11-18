# Matrix Script

Neo has a complex matrix script. The matrix script is a  X  grid of strings. It consists of alphanumeric characters, spaces and symbols (!,@,#,$,%,&).To decode the script, Neo needs to read each column and select only the alphanumeric characters andconnect them. Neo reads the column from top to bottom and starts reading from the leftmost column.If there are symbols or spaces between two alphanumeric characters of the decoded script, then Neoreplaces them with a single space '' for better readability.Neo feels that there is no need to use 'if' conditions for decoding.Alphanumeric characters consist of: [A-Z, a-z, and 0-9].Input FormatThe first line contains space-separated integers  (rows) and  (columns) respectively. The next  lines contain the row elements of the matrix script.

### ConstraintsNote: 

A  score will be awarded for using 'if' conditions in your code.

### Output Format

Print the decoded matrix script
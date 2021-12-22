'''
Given a file and assume that you can only read the file using a given method read4, implement a method read to read n characters. Your method read may be called multiple times.



Method read4:

The API read4 reads 4 consecutive characters from the file, then writes those characters into the buffer array buf.

The return value is the number of actual characters read.

Note that read4() has its own file pointer, much like FILE *fp in C.

Definition of read4:

    Parameter:  char[] buf4
    Returns:    int

Note: buf4[] is destination not source, the results from read4 will be copied to buf4[]
Below is a high level example of how read4 works:



File file("abcde"); // File is "abcde", initially file pointer (fp) points to 'a'
char[] buf = new char[4]; // Create buffer with enough space to store characters
read4(buf4); // read4 returns 4. Now buf = "abcd", fp points to 'e'
read4(buf4); // read4 returns 1. Now buf = "e", fp points to end of file
read4(buf4); // read4 returns 0. Now buf = "", fp points to end of file


Method read:

By using the read4 method, implement the method read that reads n characters from the file and store it in the buffer array buf. Consider that you cannot manipulate the file directly.

The return value is the number of actual characters read.

Definition of read:

    Parameters:	char[] buf, int n
    Returns:	int

Note: buf[] is destination not source, you will need to write the results to buf[]


Example 1:

File file("abc");
Solution sol;
// Assume buf is allocated and guaranteed to have enough space for storing all characters from the file.
sol.read(buf, 1); // After calling your read method, buf should contain "a". We read a total of 1 character from the file, so return 1.
sol.read(buf, 2); // Now buf should contain "bc". We read a total of 2 characters from the file, so return 2.
sol.read(buf, 1); // We have reached the end of file, no more characters can be read. So return 0.
Example 2:

File file("abc");
Solution sol;
sol.read(buf, 4); // After calling your read method, buf should contain "abc". We read a total of 3 characters from the file, so return 3.
sol.read(buf, 1); // We have reached the end of file, no more characters can be read. So return 0.


Note:

Consider that you cannot manipulate the file directly, the file is only accesible for read4 but not for read.
The read function may be called multiple times.
Please remember to RESET your class variables declared in Solution, as static/class variables are persisted across multiple test cases. Please see here for more details.
You may assume the destination buffer array, buf, is guaranteed to have enough space for storing n characters.
It is guaranteed that in a given test case the same buffer buf is called by read.
'''


# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.tempHold = [''] * 4
        self.tempHoldIndex = 0

    def read(self, buf: List[str], n: int) -> int:
        charRead = 0
        bufLength = 0

        read4R = 0

        # Indicator whether read from local buffer or file
        bufferRead = 0

        while charRead < n:
            buf4Placeholder = [''] * 4
            buf4 = [''] * 4
            read4Ret = 0
            # prevTemp = -1

            # If already read chars are present in tempHold
            if self.tempHoldIndex > 0:
                # prevTemp = self.tempHoldIndex - 1
                # print("Read from Temp Buffer")
                bufferRead = 1
                for index in range(self.tempHoldIndex):
                    buf4Placeholder[index] = self.tempHold[index]
                    read4Ret += 1
                    self.tempHold[index] = ''
                    self.tempHoldIndex -= 1
            else:
                bufferRead = 0
                read4R = read4(buf4)
                read4Ret += read4R
                for index in range(read4R):
                    # print(buf4[index])
                    buf4Placeholder[index] = buf4[index]
                    # prevTemp += 1
                    # charRead += read4Ret

            print("\n")
            print("self.tempHoldIndex - ", self.tempHoldIndex, " : ", self.tempHold)
            print("read4R - ", read4R, " : ", buf4)
            print("\n")
            print("Char Read - ", charRead, " :read4Ret - ", read4Ret)
            print("Buf4Placeholder - ", buf4Placeholder)

            if charRead + read4Ret <= n:
                for index in range(min(read4Ret, n)):
                    # print(buf4Placeholder[index])
                    buf[bufLength] = buf4Placeholder[index]
                    bufLength += 1
                    charRead += 1
                '''for removal in range(1, charRead-n, 1):
                    buf4Placeholder.pop()
                    charRead -= 1
                '''
            else:
                startEnd = n - charRead
                for removal in range(startEnd):
                    # print(buf4Placeholder[removal])
                    buf[bufLength] = buf4Placeholder[removal]
                    bufLength += 1
                    charRead += 1

                for index in range(startEnd, read4Ret, 1):  # 4
                    print('Increasing TempholdIndex', self.tempHoldIndex)
                    self.tempHold[self.tempHoldIndex] = buf4Placeholder[index]
                    self.tempHoldIndex += 1

            # buf.append(buf4Placeholder)
            print("Buffer - ", buf)
            print("TempHold - ", self.tempHoldIndex, self.tempHold)

            # If end of file is reached
            if bufferRead == 0:
                if read4R == 0 or read4R < 4:
                    return charRead

        return charRead
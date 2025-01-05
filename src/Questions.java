import java.util.*;

public class Questions {
    // public static int lengthOfLongestSubstring(String s) {
    //     String longestSubStr = new String();

    //     for (int j = 0; j < s.length(); j++) {
    //         String subStr = new String();

    //         for (int i = j; i < s.length(); i++) {
    //             if (subStr.indexOf(s.charAt(i)) == -1) {
    //                 subStr += s.charAt(i);
    //             } else {
    //                 break;
    //             }
    //         }

    //         if (subStr.length() > longestSubStr.length()) {
    //             longestSubStr = subStr;
    //         }
    //     }


    //     return longestSubStr.length();
    // }

    // public static void main(String[] args) {
    //     lengthOfLongestSubstring("pwwkew");
    // }
    public static int[] maxDistinctElements(int n, int[] a, int[] b, int k) {
        // Step 1: Find initial distinct elements in array a
        Set<Integer> distinctA = new HashSet<>();
        for (int num : a) {
            distinctA.add(num);
        }

        // Step 2: Find elements in b that are not in a
        Set<Integer> potentialSwaps = new HashSet<>();
        for (int num : b) {
            if (!distinctA.contains(num)) {
                potentialSwaps.add(num);
            }
        }

        // Step 3: Perform swaps to maximize distinct elements in a
        int swapCount = 0;
        for (int i = 0; i < n; i++) {
            if (swapCount >= k) {
                break;  // Stop if we've used all k swaps
            }
            if (distinctA.contains(a[i]) && !potentialSwaps.isEmpty()) {
                Iterator<Integer> it = potentialSwaps.iterator();
                int newElement = it.next();
                it.remove();
                a[i] = newElement;  // Swap the element into a
                distinctA.add(newElement);
                swapCount++;
            }
        }

        return a;  // Return the updated array
    }   

    static Integer convertHexToDecimal(String hexNumber) {
        Map<Character, Integer> hexToDec = new HashMap<>();
        hexToDec.put('0', 0);
        hexToDec.put('1', 1);
        hexToDec.put('2', 2);
        hexToDec.put('3', 3);
        hexToDec.put('4', 4);
        hexToDec.put('5', 5);
        hexToDec.put('6', 6);
        hexToDec.put('7', 7);
        hexToDec.put('8', 8);
        hexToDec.put('9', 9);
        hexToDec.put('a', 10);
        hexToDec.put('b', 11);
        hexToDec.put('c', 12);
        hexToDec.put('d', 13);
        hexToDec.put('e', 14);
        hexToDec.put('f', 15);
        
        Integer num = 0;
        char[] num_chars = hexNumber.toCharArray();
        for (int i = 0; i < num_chars.length; i++) {
            if (i == 0) {
               num = 16*hexToDec.get(num_chars[0]); 
            }
            else {
                num += hexToDec.get(num_chars[i]);
            }
        }
        return num;
    }
        
	public static void main(String[] args) {
		// int n = 5;
        // int[] a = {2, 3, 3, 2, 2};
        // int[] b = {1, 3, 2, 4, 1};
        // int k = 2;

        // int[] result = maxDistinctElements(n, a, b, k);
        // System.out.println(Arrays.toString(result));  // Output should be [2, 3, 1, 2, 4]
        System.out.println(convertHexToDecimal("1a"));
	}
}
	



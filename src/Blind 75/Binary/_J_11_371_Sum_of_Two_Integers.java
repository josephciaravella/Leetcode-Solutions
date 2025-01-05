package Binary;

public class _J_11_371_Sum_of_Two_Integers {

    public int getSum(int a, int b) {
        while (b != 0) {
            int carry = (a&b) << 1;
            a = a^b;
            b = carry;
        }

        return a;
    }
}   
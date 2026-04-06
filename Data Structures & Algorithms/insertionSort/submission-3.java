// Definition for a pair
// class Pair {
//     int key;
//     String value;
//
//     Pair(int key, String value) {
//         this.key = key;
//         this.value = value;
//     }
// }
public class Solution {
    public List<List<Pair>> insertionSort(List<Pair> pairs) {
        List<List<Pair>> sol = new ArrayList<>();
        if (pairs.size() == 0) {
            return sol;
        }
        sol.add(new ArrayList<Pair>(pairs));

        int k;
        for (int i = 1; i < pairs.size(); i++) {
            k = i;
            while (k > 0 && pairs.get(k).key < pairs.get(k-1).key) {
                Pair temp = pairs.get(k);
                pairs.set(k, pairs.get(k-1));
                pairs.set(k-1, temp);
                k--;
            }
            sol.add(new ArrayList<Pair>(pairs));
        }

        return sol;
    }
}


public class BinarySearch{

    public static void binary_search( int input_array[], int target){

        if(input_array == null){
            return;
        }

        int low = 0;
        // we want to access the array index n - 1
        int high = input_array.length-1;

        // Searhcing
        while(high >= low){
            // Clever way to calculate mid
//            int middle = (low + (high-low))/2;
            int middle = (low + high)/2;

            if(target == input_array[middle] ){
                System.out.println("Found: " + input_array[middle]);
                break;
            }else if(input_array[middle] > target) {
                high = middle - 1;
            }else{
                low = middle + 1;
            }
        }

    }


    public static void main(String[] args){
        // Binary Search on an Array
        int input_array[] = {1,2,3,4,5,6,7,8,9,10};
        int target = 4;
        binary_search(input_array, target);
    }


}
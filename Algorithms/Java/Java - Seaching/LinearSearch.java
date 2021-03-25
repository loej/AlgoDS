
public class LinearSearch{

    public static boolean linear_search(int input_array[], int target){

        if(input_array == null){
            return false;
        }
        for(int iterator = 0; iterator < input_array.length; iterator++){
            if(input_array[iterator] == target){
                return true;
            }
        }
        return false;

    }

    public static void main(String[] args){

        // Searches linear array
        int input_array[] = {1,2,3,4,5,56,10010101,29292,-991,10,3};
        boolean print_returned = linear_search(input_array, 3);
        System.out.println("Was the value found? T/F:\t"+ print_returned);

    }

}
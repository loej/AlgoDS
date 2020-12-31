/* Java - Arrays*/

public class arrays{

    // Adds two numbers (test function)
    public static int add_two_numbers(int val_one, int val_two){
        return val_one + val_two;
    }

    // Reverses Array
    public static void reverse_array(int input_array[], int array_length){
        // Array declaration
        int reversed_array[] = new int[array_length];

        for(int iterator = array_length-1; iterator >= 0; iterator--){
            reversed_array[iterator] = input_array[iterator];
            System.out.println("Index " + iterator + " \t" +  reversed_array[iterator]+ "\n");
        }

    }

    // Finding duplicate number on a given integer array and print it
    public static void find_duplicate_int(int input_array[], int array_length){

        if(input_array == null){
            return;
        }

        int duplicates = 0;

        int duplicate_array[] = new int[array_length];

        for (int pointer_one = 0; pointer_one <= array_length-1; pointer_one++ ){
            for(int pointer_two = pointer_one+1; pointer_two <= array_length-1; pointer_two++){
                if(input_array[pointer_one] == input_array[pointer_two]){
                    duplicates++;
                    duplicate_array[pointer_two] = input_array[pointer_two];
                }
            }
        }

        // Prints array with duplicates
        System.out.println(duplicates);
        System.out.println("\n");
        for(int print_i = 0; print_i <= duplicate_array.length-1; print_i++){

            if(duplicate_array[print_i] == 0){
                continue;
            }else {
                System.out.println("Duplicate Array Contents: " + duplicate_array[print_i] + "\n");
            }
        }

    }

    public static void find_largest(int input_array[]){
        int largest_element = input_array[0];

        for(int iterator = 1; iterator < input_array.length; iterator++){
            if(largest_element < input_array[iterator]){
                largest_element = input_array[iterator];
            }
        }

        System.out.println("Largest Element: " + largest_element + "\n");
    }

    public static void find_smallest(int input_array[]){
        int smallest_element = input_array[0];

        for(int iterator = 1; iterator < input_array.length; iterator++){
            if(smallest_element > input_array[iterator]){
                smallest_element = input_array[iterator];
            }
        }
        System.out.println("Smallest Element: " + smallest_element + "\n");
    }

    public static void find_largest_and_smallest(int input_array[]){

        if(input_array == null){
            return;
        }

        int largest = input_array[0];
        int smallest = input_array[0];

        for(int iterator = 1; iterator < input_array.length; iterator++){
            if(largest < input_array[iterator]){
                largest = input_array[iterator];
            }else if(smallest > input_array[iterator]){
                smallest = input_array[iterator];
            }
        }
        System.out.println("Largest Element: " + largest + "\n");
        System.out.println("Smallest Element: " + smallest + "\n");

    }




    public static void main(String[] args){
        // add_two_numbers
        System.out.println(add_two_numbers(100,100));

        System.out.println("\n");

        // Reverse Arrays
        int input_array[] = {1,2,3,4};
        reverse_array(input_array, input_array.length);

        System.out.println("\n");

        // Finding Duplicate on a given integer array
        int input_duplicate[] = {1,1,2,2,3,3};
        find_duplicate_int(input_duplicate, input_duplicate.length);

        // Finding the largest number in an unsorted array
        int input_largest[] =  {1,2,3,4,5,6,100,200,200,1000};
        find_largest(input_largest);

        // Find the smallest number in an unsorted array
        int input_smallest[] = {1,2,3,4,5,6,7,8,10,-1};
        find_smallest(input_smallest);

        // Finding the smallest and largest elements in an array
        int input_LandS[] = {1,2,3,4,5,6,100,-1,-10,89};
        find_largest_and_smallest(input_LandS);


    }


}
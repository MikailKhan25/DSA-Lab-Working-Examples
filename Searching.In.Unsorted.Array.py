// Java program to implement linear search in unsorted arrays

class Main {
    // Function to implement search operation
    static int findElement(int arr[], int n, int key) {
        for (int i = 0; i < n; i++) {
            if (arr[i] == key) {
                return i; // Return the index if found
            }
        }
        // If the key is not found
        return -1;
    }

    // Driver's Code
    public static void main(String args[]) {
        int arr[] = {12, 34, 10, 6, 40}; // Corrected array initialization
        int n = arr.length; // Length of the array
        int key = 40; // Element to search for

        // Function call
        int position = findElement(arr, n, key); // Fixed function name
        if (position == -1) {
            System.out.println("Element not found");
        } else {
            System.out.println("Element found at position: " + (position + 1)); 
        }
    }
}

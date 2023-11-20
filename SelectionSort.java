/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author rysho
 */
public class SelectionSort {
    public static void main(String arg[])
    {
        int x[] = {100, 5, 68, 14, 9, 35};
        for(int a = 0; a < x.length; a++)
        {
            System.out.print(x[a] + " ");
        }
        System.out.println();
        sort(x); //selection sort
        for(int a = 0; a < x.length; a++)
        {
            System.out.print(x[a] + " ");
        }
    }
    
    public static void sort(int x[])
    {
        for(int i = 0; i < x.length - 1; i++)
        {
            int smallestPosition = i;
            for(int j = i+1; j < x.length; j++)
            {
                if(x[j] < x[smallestPosition])
                {
                    smallestPosition = j;
                }
            }
            int temp = x[i];
            x[i] = x[smallestPosition];
            x[smallestPosition] = temp;
        }
    }
}

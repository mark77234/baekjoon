
import java.util.Scanner

fun main() {
    val sc = Scanner(System.`in`)
    while(sc.hasNextInt()) {
        val a = sc.nextInt()
        val b = sc.nextInt()

        if(a==0 && b== 0) break

        if(a>b) println("Yes")
        else println("No")
    }

}

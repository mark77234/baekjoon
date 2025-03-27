
import java.util.Scanner

fun main() {
    val sc = Scanner(System.`in`)

    val a = sc.nextBigInteger()
    val b = sc.nextBigInteger()
    val c = sc.nextBigInteger()

    println((a+b)%c)
    println(((a%c)+(b%c))%c)
    println((a*b)%c)
    println(((a%c)*(b%c))%c)

}

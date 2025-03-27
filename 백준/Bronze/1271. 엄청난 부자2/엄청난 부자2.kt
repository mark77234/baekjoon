import java.math.BigInteger

fun main(){
    val input = readln().split(" ")

    val a = BigInteger(input[0])
    val b = BigInteger(input[1])

    println(a/b)
    println(a%b)
}
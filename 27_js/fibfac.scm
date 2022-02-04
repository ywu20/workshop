;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname fibfac) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;the function named fact (for factorial) is a procedure (lambda) that takes in a parameter
; if n is less than or equal to 1, the function should return 1
; if not, the function should return the value of n times the factorial of the preceding number

(define fact
  (lambda (n)
  (if (<= n 1)
      1
  (* n (fact (- n 1))))
  )
  )
(fact 0)
(fact 1)
(fact 2)
(fact 3)
(fact 5)
(fact 10)



(define fib
  (lambda (n)
    (if (<= n 1)
        n
        (+ (fib (- n 1)) (fib ( - n 2)))
    )
  )
)

(fib 0)
(fib 1)
(fib 2)
(fib 3)
(fib 4)
(fib 5)
(fib 10)

#lang racket

; for the quadratic solver
; solves for real roots
(define (quadratic-solver a b c)
  (let* ((discriminant (- (* b b) (* 4 a c)))
         (real-part (/ (- b) (* 2 a)))
         (imaginary-part (/ (sqrt (abs discriminant)) (* 2 a))))
    (cond
      ((< discriminant 0) 
       (display "complex roots: ")
       (display (format "~a + ~ai" real-part imaginary-part))
       (display " and ")
       (display (format "~a - ~ai" real-part imaginary-part)))
      ((= discriminant 0) 
       (display "one real root: ")
       (display (/ (- b) (* 2 a))))
      (else
       (display "two real roots: ")
       (display (/ (+ (- b) (sqrt discriminant)) (* 2 a)))
       (display " and ")
       (display (/ (- (- b) (sqrt discriminant)) (* 2 a)))))))

; test cases
(display "testing quadratic equation solver with different coefficients:\n")
(display "coefficients: 1, 0, -25\n")
(quadratic-solver 1 0 -25) 
(newline)

(display "\ncoefficients: 1, 7, 12\n")
(quadratic-solver 1 7 12) 
(newline)

(display "\ncoefficients: 1, 8, 16\n")
(quadratic-solver 1 8 16) 
(newline)

(display "\ncoefficients: 2, 16, 32\n")
(quadratic-solver 2 16 32) 
(newline)

(display "\ncoefficients: 1, 2, 5\n")
(quadratic-solver 1 2 5) 
(newline)

; temp conversion
(define (f-to-c f)
  (/ (* (- f 32) 5) 9))

(define (c-to-f c)
  (+ (* c 9/5) 32))

; test cases for temp conversions
(display "\ntemperature conversion examples:\n")
(display "32°F to celsius: ")
(display (f-to-c 32))
(newline)

(display "100°F to celsius: ")
(display (f-to-c 100))
(newline)

(display "0°C to fahrenheit: ")
(display (c-to-f 0))
(newline)

(display "37°C to fahrenheit: ")
(display (c-to-f 37))
(newline)

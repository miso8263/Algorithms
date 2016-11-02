#include <assert.h>
#include <math.h>
#include <stdio.h>
#include <gmp.h>
//allows for multiprecision

using namespace std;

void Rho(mpz_t x, const mpz_t composite){
	gmp_randstate_t state1;							//generate random numbers a-la Rho's F for pseudo random numbers
	gmp_randinit_default(state1);					//f(x) = x^2 a mod N  where a is a random number
	mpz_t a;
	mpz_init(a);
	mpz_set_ui(a, 0);
	mpz_urandomm(a, state1, composite);
	
	mpz_t ans;
	mpz_init(ans);
	mpz_set_ui(ans, 0);
	mpz_pow_ui(ans, x, 2);
	
	mpz_t answer;
	mpz_init(answer);
	mpz_set_ui(answer, 0);
	mpz_mod(answer, a, composite);
	
	mpz_add(x, ans, answer);
}

int main(){
	char inputStr[1024];
	mpz_t composite;
	int flag;
	
	printf("Enter a number: ");		//take in number
	scanf("%1024s", inputStr);
	
	mpz_init(composite);					//initialize holder for composite
	mpz_set_ui(composite,0);
	
	flag = mpz_set_str(composite, inputStr, 10);		//set it as the input string interpreted as a base 10 number
	assert(flag == 0);								//need to have gotten a 0 from that
	
	mpz_t num1;
	mpz_init(num1);
	mpz_set_ui(num1, 2);
	
	mpz_t num2;
	mpz_init(num2);
	mpz_set_ui(num2, 3);
	
	mpz_t diff;
	mpz_init(diff);
	mpz_set_si(diff, 0);
	
	mpz_t abs;
	mpz_init(abs);
	mpz_set_ui(abs, 0);	

	mpz_t gcd;
	mpz_init(gcd);
	mpz_set_ui(gcd, 0);
	
	bool found = false;
	
	while(mpz_cmp(num1,num2) < 0){					//while b > a

		Rho(num1, composite);								//do Rho's things
		Rho(num2, composite);
		Rho(num2, composite);
		
		mpz_sub(diff, num2, num1);
		mpz_abs(abs, diff);
		
		mpz_gcd(gcd, abs, composite);						//compute the greatest common divisor

		if(mpz_cmp_ui(gcd, 1) > 0){
			printf("Prime factor is: ");
			mpz_out_str(stdout,10,gcd);			//output as base 10 number
			printf("\n");
			found = true;
			break;
		}
		
	}
	
	if (found == false){
		printf("Failed.  Try again.\n");
	}
	return 0;
}

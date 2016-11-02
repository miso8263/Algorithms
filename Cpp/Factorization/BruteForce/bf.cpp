#include <assert.h>
#include <math.h>
#include <stdio.h>
#include <gmp.h>
//allows for multiprecision

using namespace std;

void findOneFactor(const mpz_t x, mpz_t &a, bool &found){
	mpz_set_ui(a, 7);				//begins at 7
	
	mpz_t res;
	mpz_init(res);
	
	mpz_t two;
	mpz_init(two);

#pragma omp parallel
	while((mpz_cmp(a, x)) < 0){	
		mpz_set_ui(res, 0);
		mpz_mod(res, x, a);				//sets answer to x mod a
		
		if((mpz_cmp_d(res, 0)) == 0){	//if the modulo result is zero, we're done
			//if((mpz_probab_prime_p(a,100)) == 1){		//try for 100 reps to determine if a is probably prime
				found = true;
				break;	
			//}		
		}
		
		mpz_add(a, a, two);				//factor is factor + 2
	}
}

int main(){
	char inputStr[1024];
	mpz_t composite;
	mpz_t factor;		
	mpz_t mud;		
	int flag;
	bool found = false;
	
	
	printf("Enter a number: ");		//take in number
	if (scanf("%1024s", inputStr) != 1){
		printf("Invalid input.");
	}
	
	mpz_init(composite);					//initialize holder for composite
	mpz_set_ui(composite,0);
	mpz_init(factor);						//initialize holder for factor
	mpz_init(mud);							//initialize holder for modulo result
	
	flag = mpz_set_str(composite, inputStr, 10);		//set it as the input string interpreted as a base 10 number
	assert(flag == 0);								//need to have gotten a 0 from that
	
	while(found == false){
		//first check easy cases: 2, 3, 5
		mpz_set_ui(factor, 2);
		mpz_set_ui(mud, 0);
		
		mpz_mod(mud, composite, factor);				//sets answer to x mod a
		
		if((mpz_cmp_ui(mud, 0)) == 0){	
			found = true;
			break;
		}
		
		mpz_set_ui(factor, 3);
		mpz_set_ui(mud, 0);
		
		mpz_mod(mud, composite, factor);				
		
		if((mpz_cmp_ui(mud, 0)) == 0){	
			found = true;
			break;
		}
		
		mpz_set_ui(factor, 5);
		mpz_set_ui(mud, 0);
		
		mpz_mod(mud, composite, factor);				
		
		if((mpz_cmp_ui(mud, 0)) == 0){	
			found = true;
			break;
		}
		
		
		//didn't pass, try factoring
		findOneFactor(composite, factor, found);
		
		
	}
	
	//at this point we either found it or ran out of memory
	
	mpz_t otherfactor;
	mpz_init(otherfactor);
	mpz_cdiv_q(otherfactor,composite,factor);
	
	printf("Prime factors are: ");
	mpz_out_str(stdout,10,factor);			//output as base 10 number
	printf(" ");
	mpz_out_str(stdout,10,otherfactor);	
	printf("\n");
		
	
	return 0;
}

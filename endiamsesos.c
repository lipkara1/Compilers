include <stdio.h>

int main(){
	int  T_1,T_2,T_3,T_4,T_5;
	int temp,num,digit,sum;
L_0:
	L_1: scanf('%d',&num);
	L_2: temp=num;
	L_3: if (temp<0) goto L_5;
	L_4: goto L_14;
	L_5: T_1=temp/10;
	L_6: digit=T_1;
	L_7: T_2=digit*digit;
	L_8: T_3=T_2*digit;
	L_9: T_4=sum+T_3;
	L_10: sum=T_4;
	L_11: T_5=temp/10;
	L_12: temp=T_5;
	L_13: goto L_3;
	L_14: if (num==0) goto L_16;
	L_15: goto L_18;
	L_16: printf(" %d", num);
	L_17: goto L_19;
	L_18: printf(" %d", num);
	L_19: {}
	 exit(-1)
}
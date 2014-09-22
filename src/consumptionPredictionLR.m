%%线性回归模型
clc;clear all;close all;
num1=xlsread('fruit.xls','Sheet1','B2:B9');
num=num1';
t=2003:2010;
y=polyfit(t,num,1);
t1=2003:2020;
z=polyval(y,t1);
zz=z'
t2=2003:0.01:2020;
z1=polyval(y,t2);
plot(t,num,'bo',t2,z1,'k-')
xlabel('时间');ylabel('消费量/吨');
title('香蕉');
legend('真实值','预测值')

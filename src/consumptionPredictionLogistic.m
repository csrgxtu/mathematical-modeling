%%Logistic阻滞增长模型
close all;clear all;clc;
format long
num = xlsread('fruit.xls','Sheet1','B2:B9');
n=length(num);
dx=zeros(n,1);
for i=1:n-1
    dx(i)=(num(i+1)-num(i))/num(i); 
    end
    dx(end)=(num(end)-num(end-1))/num(end-1);
    %估计参数
    Z=[ones(n,1) num];%设计矩阵
    beta=regress(dx,Z); %最小二乘法估计r值和xm值
    r=beta(1);
    xm=-r/beta(2);
    %曲线拟合图
    s=2003:2010;
    plot(s,num(1:end),'bo')
    hold on
    s=2003:0.01:2020;
    z=xm./(1+(xm./num(1)-1)*exp(-r.*(s-2003)));
    plot(s,z,'k-')
    hold off
    xlabel('时间');ylabel('消耗量/吨');
    title('香蕉');
    legend('真实值','预测值');
    %预测值
    s1=2003:2020;
    rnum=xm./(1+(xm/num(1)-1)*exp(-r.*(s1-2003)));
    sigma=abs(rnum(1:n)-num')./num'  %相对误差
    prev=rnum(end-9:end)  %预测值

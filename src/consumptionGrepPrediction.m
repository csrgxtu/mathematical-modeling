%%灰色预测模型
clc,clear;
X1 = xlsread('fruit.xls','Sheet1','B2:B9');
X=X1';
n=length(X);%计算矩阵长度
x1=cumsum(X);%累加后的矩阵
for i=2:n
    rou(i)=X(i)/x1(i-1);%光滑性检验
    end
    for i=2:n    
        sigma(i)=x1(i)/x1(i-1);%准指数检验
        end
        i=2:n;
        y(i-1)=X(i);
        y1=y';%将原行向量转化成对应列向量
        i=1:n-1; %计算数据矩阵B的第一列数据
        C(i)=-0.5*(x1(i)+x1(i+1));
        B=[C' ones(n-1,1)];%构造矩阵B
        au=((B'*B)\B')*y1; %计算参数a,u矩阵
        au;
        a=au(1);
        u=au(2);
        i=1:n+10; %计算预测累加数列的值
        ago(i)=(X(1)-u/a)*exp(-a*(i-1))+u/a;%累加数列值
        yc(1)=ago(1);
        i=1:n+10-1; %还原数列的值
        yc(i+1)=ago(i+1)-ago(i);
        i=2:n;
        error(i)=yc(i)-X(i);%计算  残差值
        yc(1)=ago(1);
        i=1:n;%修正的还原数列值
        yc(i+1)=ago(i+1)-ago(i);%预测值
        c=std(error)/std(X);%计算后验差比
        p=0;
        for i=1:2n
            if(abs(error(i)-mean(error))<0.6745*std(X))
                    p=p+1;
                        end
                        end
                        p=p/(n-1);%小误差概率
                        w1=min(abs(error));
                        w2=max(abs(error));
                        i=1:n;
                        w(i)=(w1+0.5*w2)./(abs(error(i))+0.5*w2);
                        w=sum(w)/(n);%关联度
                        disp('光滑性检验')
                        rou%光滑性检验
                        disp('准指数检验')
                        sigma%准指数检验
                        disp('参数a,u')
                        au   %参数a,u
                        disp('累加数列ago的值')
                        %ago  %累加数列ago的值
                        x1
                        disp('原始序列')
                        X    %原始序列
                        disp('预测数值')
                        yc   %预测数值
                        disp('残差值')
                        error%残差值
                        disp('后验差比值')
                        c    %后验差比值
                        disp('小误差概率的值')
                        p    %小误差概率的值
                        disp('关联度')
                        w    %关联度w
                        QQ=abs((error./X)*100)%相对误差百分比

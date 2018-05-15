clear;
R=[-1 -1 -1 -1 0 -1
   -1 -1 -1 0 -1 100
   -1 -1 -1 0 -1 -1
   -1  0  0 -1 0 -1
    0 -1 -1 0 -1 100
   -1  0 -1 -1 0 100    ]
Q=[ 0 0 0 0 0 0 
    0 0 0 0 0 0
    0 0 0 0 0 0
    0 0 0 0 0 0
    0 0 0 0 0 0
    0 0 0 0 0 0    ]

for k=1:5000
for i=1:6
    for j=1:6
        newmax=0;
        for i1=1:6
            if(R(j,i1)>-1)
                newmax=max(newmax,Q(j,i1));
            end
        end
        if(R(i,j)>-1)
            Q(i,j)=R(i,j)+0.8*newmax;
        end
    end
end
end
Q
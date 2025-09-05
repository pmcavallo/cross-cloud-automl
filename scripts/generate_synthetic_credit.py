import argparse, os, numpy as np, pandas as pd, yaml
TARGET='default_12m'
NUMERIC=['income','dti','ltv','utilization','inquiries_12m','age','tenure_months','credit_lines']
CATEG=['state','channel','segment','synthetic_group']
def make_data(n,seed):
    rng=np.random.default_rng(seed)
    df=pd.DataFrame({"income":rng.lognormal(10.5,0.5,n),"dti":np.clip(rng.normal(0.3,0.15,n),0,1),"ltv":np.clip(rng.normal(0.7,0.2,n),0,2),"utilization":rng.beta(2,5,n),"inquiries_12m":rng.poisson(1.5,n),"age":np.clip(rng.normal(42,12,n),18,90),"tenure_months":np.clip(rng.normal(60,40,n),0,360),"credit_lines":np.clip(rng.normal(8,4,n),1,30),"state":rng.choice(['CA','TX','NY','FL'],n),"channel":rng.choice(['branch','online','partner'],n),"segment":rng.choice(['prime','near_prime','subprime'],n),"synthetic_group":rng.choice(['A','B'],n)})
    z=0.8*(df['dti']-0.3)+0.6*(df['ltv']-0.7)+1.2*(df['utilization']-0.4)
    p=1/(1+np.exp(-z))
    df[TARGET]=(rng.uniform(0,1,n)<p).astype(int)
    return df
def split(df,seed):
    rng=np.random.default_rng(seed); idx=rng.permutation(len(df)); n=len(df)
    return df.iloc[idx[:int(.7*n)]],df.iloc[idx[int(.7*n):int(.85*n)]],df.iloc[idx[int(.85*n):]]
def write_schema(path):
    schema={'target':TARGET,'numeric':NUMERIC,'categorical':CATEG,'sensitive':['synthetic_group']}
    os.makedirs(os.path.dirname(path),exist_ok=True)
    with open(path,'w') as f: yaml.safe_dump(schema,f)
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--rows',type=int,default=5000); ap.add_argument('--seed',type=int,default=42); ap.add_argument('--outdir',default='data'); args=ap.parse_args()
    df=make_data(args.rows,args.seed)
    tr,va,te=split(df,args.seed)
    os.makedirs(args.outdir,exist_ok=True)
    tr.to_csv(f'{args.outdir}/train.csv',index=False); va.to_csv(f'{args.outdir}/valid.csv',index=False); te.to_csv(f'{args.outdir}/test.csv',index=False)
    write_schema(f'{args.outdir}/schema.yaml')
    print('Generated dataset with',len(tr),'train,',len(va),'valid,',len(te),'test rows.')

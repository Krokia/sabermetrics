from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import backend.calc_baseball as bball

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class ObpRequest(BaseModel):
    H: int
    BB: int
    GP: int
    VB: int
    SH:int

class SlgRequest(BaseModel):
    VB: int
    single: int
    double: int
    triple: int
    HR: int
    
class OpsRequest(BaseModel):
    H: int
    BB: int
    GP: int
    VB:int 
    SH: int
    single: int
    double: int
    triple: int
    HR: int
    
class K9Request(BaseModel):
    K: int
    IP: int

class FipRequest(BaseModel):
    HR: int
    BB: int
    GP: int
    IBB: int
    K: int
    IP: int
    
class BabipRequest(BaseModel):
    H: int
    HR: int
    K: int
    SF: int
    TB: int

@app.post("/calc_obp")
def calculate(request: ObpRequest):
    H = request.H
    BB = request.BB
    GP = request.GP
    VB = request.VB
    SH = request.SH
    
    result = bball.calc_obp(H, BB, GP, VB, SH)
    return {"result": result}

@app.post("/calc_slg")
def calculate(request: SlgRequest):
    VB = request.VB
    single = request.single
    double = request.double
    triple = request.triple
    HR = request.HR
    
    result = bball.calc_slg(VB, single, double, triple, HR)
    return {"result": result}

@app.post("/calc_ops")
def calculate(request: OpsRequest):
    H = request.H
    BB = request.BB
    GP = request.GP
    VB = request.VB
    SH = request.SH
    VB = request.VB
    single = request.single
    double = request.double
    triple = request.triple
    HR = request.HR
    
    result = bball.calc_ops(H, BB, GP, VB, SH, single, double, triple, HR)
    return {"result": result}

@app.post("/calc_k9")
def calculate(request: K9Request):
    K = request.K
    IP = request.IP
    
    result = bball.calc_k9(K, IP)
    return {"result": result}

@app.post("/calc_fip")
def calculate(request: FipRequest):
    HR = request.HR
    BB = request.BB
    GP = request.GP
    IBB = request.IBB
    K = request.K
    IP = request.IP
    
    result = bball.calc_fip(HR, BB, GP, IBB, K, IP)
    return {"result": result}

@app.post("/calc_babip")
def calculate(request: BabipRequest):
    H = request.H
    HR = request.HR
    K = request.K
    SF = request.SF
    TB = request.TB
    
    result = bball.calc_babip(H, HR, K, SF, TB)
    return {"result": result}

@app.get("/help")
def help():
    return {"message": "You dont need help!"}
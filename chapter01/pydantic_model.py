from typing import Union, Optional, Literal

from pydantic import BaseModel, Field, ValidationError, field_validator, model_validator, computed_field
from enum import Enum

class Status(str, Enum):
	Pending = "Pending"
	Accepted = "Accepted"
	Rejected = "Rejected"

class SimpleUser(BaseModel):
	id: int = Field(..., gt=0, description="用户ID")
	name: str
	payload: Union[int, str]
	flag: Optional[bool] = None
	status: Status
	level: Literal["Pending", "Accepted", "Rejected"] = "Pending"
	start_ts: int
	end_ts: int
	model_config = {
		"str_strip_whitespace": True,
		"str_to_lower": True,
		"extra": "forbid"
	}
	
	@model_validator(mode="after")
	def check_time(self):
		
		if self.start_ts > self.end_ts:
			raise ValueError("时间不合理")
		
		return self
	
	@computed_field(return_type=int)
	def time_diff(self):
		return self.end_ts - self.start_ts
	
	# field_validator 必须是cls级别的
	# @field_validator("name", mode="before")
	# def trim_name(cls, val):
	# 	if isinstance(val, str):
	# 		val = val.strip()
	# 	if not val:
	# 		raise ValueError("姓名不能为空")
	# 	return val

def generate_user():
	try:
		u = SimpleUser(id=1, name=" ", payload="Xiao. ", flag=True, status=Status.Accepted, level="Accepted", start_ts=3, end_ts=6)
		print(u.model_dump_json())
	except ValidationError as e:
		print("Validation error:", e)
		
		
if __name__ == '__main__':
	generate_user()
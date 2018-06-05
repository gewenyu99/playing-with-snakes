Promise.resolve(()=>{
  return 0;
}).then(()=>{
	console.log(1);
}).then(() => {
  console.log(1);
}
);
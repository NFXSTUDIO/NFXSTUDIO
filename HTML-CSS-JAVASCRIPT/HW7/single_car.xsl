<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">

    <xsl:template match="/">
        <html>
            <body>
                <h1>Car Details</h1>
                <xsl:apply-templates select="catalog/car[1]" />
            </body>
        </html>
    </xsl:template>

    <xsl:template match="car">
        <div style="border: 1px solid #ccc; padding: 10px; margin: 10px;">
            <h2><xsl:value-of select="make" /> <xsl:value-of select="model" /></h2>
            <p>Year: <xsl:value-of select="year" /></p>
            <p>Color: <xsl:value-of select="color" /></p>
            <p>Number of Doors: <xsl:value-of select="number_of_doors" /></p>
            <p>Transmission: <xsl:value-of select="transmission_type" /></p>
        </div>
    </xsl:template>

</xsl:stylesheet>

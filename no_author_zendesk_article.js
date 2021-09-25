$('.search-result-meta').each(function() {

var noAuthorSearchMeta = $(this).html();

noAuthorSearchMeta = "\n    posted " + noAuthorSearchMeta.substring(noAuthorSearchMeta.indexOf("<time"));

$(this).html(noAuthorSearchMeta);

});
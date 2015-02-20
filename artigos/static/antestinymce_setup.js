
function encodeURIforLinkto(value) {
  return encodeURI(value.toString().toLowerCase()
    .replace(/^\s+|\s+$/g, '')      // Trim
    .replace(/\s+/g, '-')           // Replace spaces with -
    .replace(/\-\-+/g, '-')         // Replace multiple - with single -
    )
}

function CustomFileBrowser(field_name, url, type, win) {
    
    var cmsURL = '/admin/filebrowser/browse/?pop=2';
    cmsURL = cmsURL + '&type=' + type;
    
    tinyMCE.activeEditor.windowManager.open({
        file: cmsURL,
        width: 980,  // Your dimensions may differ - toy around with them!
        height: 500,
        resizable: 'yes',
        scrollbars: 'yes',
        inline: 'no',  // This parameter only has an effect if you use the inlinepopups plugin!
        close_previous: 'no'
    }, {
        window: win,
        input: field_name,
        editor_id: tinyMCE.selectedInstance.editorId
    });
    return false;
}

tinyMCE.init({
    
    // see http://www.tinymce.com/wiki.php/Configuration
    
    // Init
    mode: 'textareas',
    theme: 'advanced',
    skin: 'default',
    
    // General
    entity_encoding: 'raw',
    // entity_encoding: 'named', // vai trocar todos acentos por entities
    verify_html: true,
    accessibility_warnings: false,
    browsers: 'gecko,msie,safari,opera',
    editor_deselector: 'mceNoEditor',
    keep_styles: false,
    language: 'en',
    object_resizing: true,
    plugins: 'advimage,advlink,paste,media,searchreplace,template,contextmenu,table,inlinepopups,youtubeIframe,visualchars',
    tools: 'inserttable',
    // directionality : "rtl",
    dialog_type: 'modal', // inlinepopups
    
    // Callbacks
    file_browser_callback: 'CustomFileBrowser',
    
    // Cleanup/Output
    element_format: 'html',
    fix_list_elements: true,
    forced_root_block: 'p',
    // style formsts overrides theme_advanced_styles
    // see http://www.tinymce.com/wiki.php/Configuration:style_formats
    style_formats: [
        //{title: 'Paragraph Small', block : 'p', classes: 'p_small'},
        //{title: 'Paragraph ImageCaption', block : 'p', classes: 'p_caption'},
        {title: 'Cinza', block : 'p', classes: 'muted'},
        {title: 'Lead', block : 'p', classes: 'lead'},
        {title: 'Legenda', inline : 'small', classes: 'muted'},
        {title: 'Label Default', inline : 'span', classes: 'label'},
        {title: 'Label Success', inline : 'span', classes: 'label label-success'},
        {title: 'Label Warning', inline : 'span', classes: 'label label-warning'},
        {title: 'Label Important', inline : 'span', classes: 'label label-important'},
        {title: 'Label Info', inline : 'span', classes: 'label label-info'},
        {title: 'Label Inverse', inline : 'span', classes: 'label label-inverse'}
    ],
    verify_html: true,

    // URL
    relative_urls: false,
    document_base_url : "/",
    remove_script_host: true,

    // Layout
    width: 758,
    height: 400,
    indentation: '10px',
    
    // Content CSS
    // customize your content ...
    content_css : "/static/bootstrap/css/bootstrap.min.css,/static/tinymce_content.min.css",
    
    // Theme Advanced
    theme_advanced_toolbar_location: 'top',
    theme_advanced_toolbar_align: 'left',
    theme_advanced_statusbar_location: 'bottom',
    theme_advanced_buttons1: 'formatselect,styleselect,|,bold,italic,underline,|,bullist,numlist,blockquote,sub,sup,|,undo,redo,|,hr,justifyleft,justifycenter,justifyright,justifyfull,|,indent,outdent,|,link,unlink,|,image,charmap,visualchars',
    theme_advanced_buttons2: 'search,|,cut,copy,paste,pasteword,|,media,youtubeIframe,|,table,tablecontrols,|,removeformat,cleanup,code',
    theme_advanced_buttons3: 'linkto_bio,linkto_event,linkto_place,|,image_caption_left,image_caption_right,|,columns_4x4,columns_2x2x2x2,columns_2x6,columns_6x2',
    theme_advanced_path: false,
    theme_advanced_blockformats: 'p,h2,h3,h4,pre,code',
    theme_advanced_resizing: true,
    theme_advanced_resize_horizontal: false,
    theme_advanced_resizing_use_cookie: true,
    
    // Image Plugin
    // see http://www.tinymce.com/wiki.php/Plugin:advimage
    theme_advanced_styles: 'Image Left=img_left;Image Right=img_right;Image Block=img_block',
    advimage_update_dimensions_onchange: true,
    
    table_styles: 'Table=table;Stripped=table table-striped;Bordered=table table-bordered;Condensed=table table-condensed',
    table_row_styles: 'Success=success;Error=error;Warning=warning;Info=info',
    //table_cell_styles: '',

    // Link Settings
    // see http://www.tinymce.com/wiki.php/Plugin:advlink
    advlink_styles: 'Internal Link=internal;External Link=external',

    // Media Plugin
    // see http://www.tinymce.com/wiki.php/Plugin:media
    media_strict: true,
    
    // Grappelli Settings
    grappelli_adv_hidden: false,
    grappelli_show_documentstructure: 'on',


    setup : function(ed) {
        // Add a custom button
        ed.addButton('linkto_bio', {
            title : 'Link to Bio',
            image : '/static/img/tinymce_linkto_bio.png',
            onclick : function() {
                // Add you own code to execute something on click
                ed.focus();
                //ed.selection.setContent('Hello world!');
                texto = ed.selection.getContent();
                slug = texto.replace(/^\s+|\s+$/g,""); // trim
                slug = slug.replace(/\s+/g,"-"); // slug
                slug.toLowerCase();
                ed.selection.setContent('<a href="/bio/' + encodeURIforLinkto(slug) + '.html" class="linkto linkto_bio">' + texto + '</a>');
            }
        });

        ed.addButton('linkto_place', {
            title : 'Link to Place',
            image : '/static/img/tinymce_linkto_place.png',
            onclick : function() {
                // Add you own code to execute something on click
                ed.focus();
                //ed.selection.setContent('Hello world!');
                texto = ed.selection.getContent();
                slug = texto.replace(/^\s+|\s+$/g,""); // trim
                slug = slug.replace(/\s+/g,"-"); // slug
                slug.toLowerCase();
                ed.selection.setContent('<a href="/lugares/' + encodeURIforLinkto(slug) + '.html" class="linkto linkto_place">' + texto + '</a>');
            }
        });

        ed.addButton('linkto_event', {
            title : 'Link to Event',
            image : '/static/img/tinymce_linkto_event.png',
            onclick : function() {
                // Add you own code to execute something on click
                ed.focus();
                //ed.selection.setContent('Hello world!');
                texto = ed.selection.getContent();
                slug = texto.replace(/^\s+|\s+$/g,""); // trim
                slug = slug.replace(/\s+/g,"-"); // slug
                slug.toLowerCase();
                ed.selection.setContent('<a href="/eventos/' + encodeURIforLinkto(slug) + '.html" class="linkto linkto_event">' + texto + '</a>');
            }
        });


        ed.addButton('image_caption_left', {
            title : 'Imagem com caption pra esquerda',
            image : '/static/img/tinymce_image_left.png',
            onclick : function() {
                ed.focus();
                texto = ed.selection.getContent();
                ed.selection.setContent('<div class="img_left span4 figure"><img src="/static/img/tinymce_image_left.png" alt=""><p class="figcaption">Caption ' + texto + '</p></div>');
            }
        });

        ed.addButton('image_caption_right', {
            title : 'Imagem com caption pra direita',
            image : '/static/img/tinymce_image_right.png',
            onclick : function() {
                ed.focus();
                texto = ed.selection.getContent();
                ed.selection.setContent('<div class="img_right span4 figure"><img src="/static/img/tinymce_image_right.png" alt=""><p class="figcaption">Caption ' + texto + '</p></div>');
            }
        });

        // ed.addButton('columns_2', {
        //     title : 'Duas colunas',
        //     image : '/static/img/tinymce_image_right.png',
        //     onclick : function() {
        //         ed.focus();
        //         ed.selection.setContent('<table class="table"><tr><td class="span4">1</td><td class="span4">2</td></tr></table>');
        //     }
        // });

        ed.addButton('columns_4x4', {
            title : 'Duas colunas (4+4)',
            image : '/static/img/tinymce_columns_4x4.png',
            onclick : function() {
                ed.focus();
                ed.selection.setContent('<div class="row"><div class="span4">1</div><div class="span4">2</div></div>');
            }
        });

        ed.addButton('columns_2x2x2x2', {
            title : 'Quatro colunas (2+2+2+2)',
            image : '/static/img/tinymce_columns_2x2x2x2.png',
            onclick : function() {
                ed.focus();
                ed.selection.setContent('<div class="row"><div class="span2">1</div><div class="span2">2</div><div class="span2">3</div><div class="span2">4</div></div>');
            }
        });

        ed.addButton('columns_6x2', {
            title : 'Duas colunas (6+2)',
            image : '/static/img/tinymce_columns_6x2.png',
            onclick : function() {
                ed.focus();
                ed.selection.setContent('<div class="row"><div class="span6">1</div><div class="span2">2</div></div>');
            }
        });

        ed.addButton('columns_2x6', {
            title : 'Duas colunas (2+6)',
            image : '/static/img/tinymce_columns_2x6.png',
            onclick : function() {
                ed.focus();
                ed.selection.setContent('<div class="row"><div class="span2">1</div><div class="span6">2</div></div>');
            }
        });


    }
    
    // Elements
    // valid_elements: '@[id|class|style|title|dir<ltr?rtl|lang|xml::lang|onclick|ondblclick|'
    // + 'onmousedown|onmouseup|onmouseover|onmousemove|onmouseout|onkeypress|'
    // + 'onkeydown|onkeyup],a[rel|rev|charset|hreflang|tabindex|accesskey|type|'
    // + 'name|href|target|title|class|onfocus|onblur],strong/b,em/i,strike,u,'
    // + '#p,-ol[type|compact],-ul[type|compact],-li,br,img[longdesc|usemap|'
    // + 'src|border|alt=|title|hspace|vspace|width|height|align],-sub,-sup,'
    // + '-blockquote,-table[border=0|cellspacing|cellpadding|width|frame|rules|'
    // + 'height|align|summary|bgcolor|background|bordercolor],-tr[rowspan|width|'
    // + 'height|align|valign|bgcolor|background|bordercolor],tbody,thead,tfoot,'
    // + '#td[colspan|rowspan|width|height|align|valign|bgcolor|background|bordercolor'
    // + '|scope],#th[colspan|rowspan|width|height|align|valign|scope],caption,-div,'
    // + '-span,-code,-pre,address,-h1,-h2,-h3,-h4,-h5,-h6,hr[size|noshade],-font[face'
    // + '|size|color],dd,dl,dt,cite,abbr,acronym,del[datetime|cite],ins[datetime|cite],'
    // + 'object[classid|width|height|codebase|*],param[name|value|_value],embed[type|width'
    // + '|height|src|*],script[src|type],map[name],area[shape|coords|href|alt|target],bdo,'
    // + 'button,col[align|char|charoff|span|valign|width],colgroup[align|char|charoff|span|'
    // + 'valign|width],dfn,fieldset,form[action|accept|accept-charset|enctype|method],'
    // + 'input[accept|alt|checked|disabled|maxlength|name|readonly|size|src|type|value],'
    // + 'kbd,label[for],legend,noscript,optgroup[label|disabled],option[disabled|label|selected|value],'
    // + 'q[cite],samp,select[disabled|multiple|name|size],small,'
    // + 'textarea[cols|rows|disabled|name|readonly],tt,var,big',
    // extended_valid_elements : 'embed[width|height|name|flashvars|src|bgcolor|align|play|'
    // + 'loop|quality|allowscriptaccess|type|pluginspage]'
    
});

